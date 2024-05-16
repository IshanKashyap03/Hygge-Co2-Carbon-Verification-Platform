// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract CertificateFactory{

    address public publisher;

    uint certificateId = 0;

    struct Certificate{
        uint uuid;
        address owner;
        bytes32 computedHash;
        uint amount;
    }

    mapping(bytes32 => Certificate) public certificates;
    mapping(bytes32 => mapping(uint => bool)) public hashAndAmount;

    constructor(){
        publisher = msg.sender;
    }

    function createCertificate(bytes32 computedHash, uint amount) public returns (bytes32){
        certificateId++;
        Certificate memory newCertificate = Certificate(certificateId, msg.sender, computedHash, amount);
        // Encoding the certificate to bytes and then hashing it
        bytes32 hash = keccak256(abi.encode(newCertificate.uuid, newCertificate.owner, newCertificate.computedHash, newCertificate.amount));
        certificates[hash] = newCertificate;
        hashAndAmount[hash][amount] = true;
        return hash;
    }

    // for the regulator
    function verifyCertificateByHashAndAmount(bytes32 hash, uint amount) public view returns(bool){
        if(hashAndAmount[hash][amount] == true){
            return true;
        }
        return false;
    }


    
}