// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "./CO2EmissionCertificate.sol";

contract CertificateFactory{

    address public publisher;

    mapping(bytes32 => CO2EmissionCertificate) public certificates;

    event CertificateCreated(address owner, bytes32 computedHash, bytes32 verificationHash);

    constructor() {
        publisher = msg.sender;
    }

    modifier onlyPublisher() {
        require(publisher == msg.sender, "Only the publisher can call this method");
        _;
    }

    function createCertificate(bytes32 computedHash, bytes32 verificationHash) public onlyPublisher {
        CO2EmissionCertificate newCertificate = new CO2EmissionCertificate(uuid, msg.sender, computedHash, amount);
        certificates[verificationHash] = newCertificate;

        emit CertificateCreated(msg.sender, computedHash, verificationHash);
    }

    function verifyCertificateByUuidAndAmount(bytes32 verificationHash) public view returns (bool) {
        CO2EmissionCertificate certificate = certificates[verificationHash];
        return address(certificate) != address(0);
    }
}
