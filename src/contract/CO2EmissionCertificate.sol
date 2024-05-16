// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract CO2EmissionCertificate {
    address public publisher;
    bytes32 public computedHash;

    constructor(address _publisher, bytes32 _computedHash) {
        publisher = _publisher;
        computedHash = _computedHash;
    }
}
