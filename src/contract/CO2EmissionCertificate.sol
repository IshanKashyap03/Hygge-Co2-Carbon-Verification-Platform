// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract CO2EmissionCertificate {
    string public uuid;
    address public owner;
    bytes32 public computedHash;
    uint public amount;

    constructor(string memory _uuid, address _owner, bytes32 _computedHash, uint _amount) {
        uuid = _uuid;
        owner = _owner;
        computedHash = _computedHash;
        amount = _amount;
    }
}