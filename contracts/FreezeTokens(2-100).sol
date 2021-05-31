pragma solidity ^0.8.4;
// SPDX-License-Identifier: UNLICENSED
// owner = 0x7ccd779fB7A0913fCBdb8b37DB812A57c9592632
// x-token (main) = 0x19c97782077d70a37988a304ff5591a7063b510f

interface IBEP20 {
    /**
     * @dev Returns the amount of tokens in existence.
     */
    function totalSupply() external view returns (uint256);

    /**
     * @dev Returns the token decimals.
     */
    function decimals() external view returns (uint8);

    /**
     * @dev Returns the token symbol.
     */
    function symbol() external view returns (string memory);

    /**
    * @dev Returns the token name.
    */
    function name() external view returns (string memory);

    /**
    * @dev Returns the bep token owner.
    */
    function getOwner() external view returns (address);

    /**
     * @dev Returns the amount of tokens owned by `account`.
     */
    function balanceOf(address account) external view returns (uint256);

    /**
     * @dev Moves `amount` tokens from the caller's account to `recipient`.
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * Emits a {Transfer} event.
     */
    function transfer(address recipient, uint256 amount) external returns (bool);

    /**
     * @dev Returns the remaining number of tokens that `spender` will be
     * allowed to spend on behalf of `owner` through {transferFrom}. This is
     * zero by default.
     *
     * This value changes when {approve} or {transferFrom} are called.
     */
    function allowance(address owner, address spender) external view returns (uint256);

    /**
     * @dev Sets `amount` as the allowance of `spender` over the caller's tokens.
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * IMPORTANT: Beware that changing an allowance with this method brings the risk
     * that someone may use both the old and the new allowance by unfortunate
     * transaction ordering. One possible solution to mitigate this race
     * condition is to first reduce the spender's allowance to 0 and set the
     * desired value afterwards:
     * https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729
     *
     * Emits an {Approval} event.
     */
    function approve(address spender, uint256 amount) external returns (bool);

    /**
     * @dev Moves `amount` tokens from `sender` to `recipient` using the
     * allowance mechanism. `amount` is then deducted from the caller's
     * allowance.
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * Emits a {Transfer} event.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    /**
     * @dev Emitted when `value` tokens are moved from one account (`from`) to
     * another (`to`).
     *
     * Note that `value` may be zero.
     */
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Emitted when the allowance of a `spender` for an `owner` is set by
     * a call to {approve}. `value` is the new allowance.
     */
    event Approval(address indexed owner, address indexed spender, uint256 value);
}


abstract contract Context {
    function _msgSender() internal view virtual returns (address) {
        return msg.sender;
    }

    function _msgData() internal view virtual returns (bytes calldata) {
        this; // silence state mutability warning without generating bytecode - see https://github.com/ethereum/solidity/issues/2691
        return msg.data;
    }
}

contract Ownable is Context {
    address private _owner;

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Initializes the contract setting the deployer as the initial owner.
     */
    constructor (address _tokenOwner) {
        _owner = _tokenOwner;
        emit OwnershipTransferred(address(0), _owner);
    }

    /**
     * @dev Returns the address of the current owner.
     */
    function owner() public view returns (address) {
        return _owner;
    }

    /**
     * @dev Throws if called by any account other than the owner.
     */
    modifier onlyOwner() {
        require(_owner == _msgSender(), "Ownable: caller is not the owner");
        _;
    }

    /**
     * @dev Leaves the contract without owner. It will not be possible to call
     * `onlyOwner` functions anymore. Can only be called by the current owner.
     *
     * NOTE: Renouncing ownership will leave the contract without an owner,
     * thereby removing any functionality that is only available to the owner.
     */
    function renounceOwnership() public onlyOwner {
        emit OwnershipTransferred(_owner, address(0));
        _owner = address(0);
    }

    /**
     * @dev Transfers ownership of the contract to a new account (`newOwner`).
     * Can only be called by the current owner.
     */
    function transferOwnership(address newOwner) public onlyOwner {
        _transferOwnership(newOwner);
    }

    /**
     * @dev Transfers ownership of the contract to a new account (`newOwner`).
     */
    function _transferOwnership(address newOwner) internal {
        require(newOwner != address(0), "Ownable: new owner is the zero address");
        emit OwnershipTransferred(_owner, newOwner);
        _owner = newOwner;
    }
}

contract FreezeTokens is Context, Ownable {

    uint256 public freezePeriod;
    uint256 public seek;

    uint256 public numerator;
    uint256 public denominator;

    IBEP20 public token;

    uint256 public startDay;
    bool public isProcessedFreeze;

    uint256 public balanceFreezeTokens;
    uint256 public balanceReturnedTokens;

    event SetToken(address indexed previousToken, address indexed newToken);
    event SetParameter(uint256 oneValue, uint256 twoValue, uint256 oldOneValue, uint256 oldTwoValue, string info);
    event Freeze(uint256 amount, uint256 date);
    event UnFreeze(uint256 amount, uint256 date);

    constructor (address _owner, address _token) Ownable(_owner) {
        require(_owner != address(0), "FreezeTokens: wrong value for address owner");
        require(_token != address(0), "FreezeTokens: wrong value for address token");

        emit SetToken(address(0), _token);
        token = IBEP20(_token);

        emit SetParameter(60*60*24*120, 60*60*24*7, freezePeriod, seek, "set freezePeriod & seek");
        freezePeriod = 60*60*24*120;
        seek = 60*60*24*7;

        emit SetParameter(2, 100, numerator, denominator, "set numerator & denominator");
        numerator = 2;
        denominator = 100;
    }

    function setToken(address _newToken) external onlyOwner {
        require(_newToken != address(0), "FreezeTokens: transfer from the zero address");
        emit SetToken(address(token), _newToken);
        token = IBEP20(_newToken);
    }

    function setTimeParameter(uint256 _freezePeriod, uint256 _seek) external onlyOwner {
        require(!isProcessedFreeze, "FreezeTokens: is processed freeze");
        emit SetParameter(_freezePeriod, _seek, freezePeriod, seek, "set freezePeriod & seek");
        freezePeriod = _freezePeriod;
        seek = _seek;
    }

    function setPercentParameter(uint256 _numerator, uint256 _denominator) external onlyOwner {
        require(!isProcessedFreeze, "FreezeTokens: is processed freeze");
        emit SetParameter(_numerator, _denominator, numerator, denominator, "set numerator & denominator");
        numerator = _numerator;
        denominator = _denominator;
    }

    function freeze(uint256 _amount) external onlyOwner {
        require(!isProcessedFreeze, "FreezeTokens: Freeze not turned off");
        isProcessedFreeze = true;
        require(token.transferFrom(_msgSender(), address(this), _amount), "FreezeTokens: failed transfer tokens");

        balanceFreezeTokens = _amount;
        startDay = block.timestamp;
        emit Freeze(_amount, startDay);
    }

    function unFreeze(uint256 _amount) external onlyOwner {
        require(isProcessedFreeze, "FreezeTokens: Freeze not turned on");
        require(checkUnFreezeAmount() >= _amount, "FreezeTokens: Freeze not turned on");

        require(token.transfer(_msgSender(), _amount), "FreezeTokens: failed transfer tokens");
        balanceReturnedTokens += _amount;
        emit UnFreeze(_amount, block.timestamp);
    }


    function checkUnFreezeAmount() public view returns(uint256 _available) {
        uint256 passedTime = block.timestamp - startDay;
        uint256 balance = token.balanceOf(address(this));
        if (passedTime > freezePeriod && isProcessedFreeze && balance > 0) {
            uint256 weeksCount = (passedTime - freezePeriod) / seek;
            uint256 part = balanceFreezeTokens * numerator / denominator;
            if (balance < part) {
                _available = balance;
            } else {
                uint256 accrued = weeksCount * part;
                if (accrued > balanceReturnedTokens) {
                    _available = accrued - balanceReturnedTokens;
                    if(_available > balance) {
                        _available = balance;
                    }
                }
            }
        }
    }

    function clear() external onlyOwner {
        if (balanceFreezeTokens == balanceReturnedTokens && isProcessedFreeze) {
            balanceFreezeTokens = 0;
            balanceReturnedTokens = 0;
            isProcessedFreeze = false;
            startDay = 0;
        }
    }
}
