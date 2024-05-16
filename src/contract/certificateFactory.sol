// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "./CO2EmissionCertificate.sol";

contract CertificateFactory{

    address public publisher;

    mapping(string => CO2EmissionCertificate) public certificates;
    mapping(string => mapping(uint => bool)) public uuidAndAmount;

    event CertificateCreated(string uuid, address owner, bytes32 computedHash, uint amount);

    constructor() {
        publisher = msg.sender;
    }

    function createCertificate(string memory uuid, bytes32 computedHash, uint amount) public{
        require(msg.sender == publisher, "Only the publisher can create certificates");
        require(amount > 0, "Amount must be greater than zero");
        
        CO2EmissionCertificate newCertificate = new CO2EmissionCertificate(uuid, msg.sender, computedHash, amount);
        certificates[uuid] = newCertificate;
        uuidAndAmount[uuid][amount] = true;
        
        emit CertificateCreated(uuid, msg.sender, computedHash, amount);
    }

    function verifyCertificateByUuidAndAmount(string memory uuid, uint amount) public view returns (bool) {
        require(uuidAndAmount[uuid][amount], "Certificate not found");
        return true;
    }
}
