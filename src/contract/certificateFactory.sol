// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract CertificateFactory{

    address public publisher;
    uint public certificateId = 0;

    struct Certificate {
        uint uuid;
        address owner;
        bytes32 computedHash;
        uint amount;
    }

    mapping(bytes32 => Certificate) public certificates;
    mapping(bytes32 => mapping(uint => bool)) public hashAndAmount;

    event CertificateCreated(uint uuid, address owner, bytes32 computedHash, uint amount);

    constructor() {
        publisher = msg.sender;
    }

    function createCertificate(bytes32 computedHash, uint amount) public returns (bytes32) {
        require(msg.sender == publisher, "Only the publisher can create certificates");
        require(amount > 0, "Amount must be greater than zero");
        
        bytes32 hash = keccak256(abi.encode(certificateId, msg.sender, computedHash, amount));
        certificateId++;
        Certificate memory newCertificate = Certificate(certificateId, msg.sender, computedHash, amount);
        certificates[hash] = newCertificate;
        hashAndAmount[hash][amount] = true;
        
        emit CertificateCreated(newCertificate.uuid, newCertificate.owner, newCertificate.computedHash, newCertificate.amount);
        return hash;
    }

    // for the regulator
    function verifyCertificateByHashAndAmount(bytes32 hash, uint amount) public view returns (bool) {
        // Check if the certificate exists
        require(hashAndAmount[hash][amount], "Certificate not found");
        return true;
    }
}
