// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract CertificateFactory{

    address public publisher;

    uint certificateId = 0;

    struct Certificate{
        uint uuid;
        address owner;
        uint256 startTime;
        uint256 endTime;
        uint amount;
    }

    mapping(bytes32 => Certificate) public certificates;
    mapping(bytes32 => mapping(uint => bool)) public hashAndAmount;

    constructor(){
        publisher = msg.sender;
    }

    function createCertificate(uint256 startTime, uint256 endTime, uint amount) public returns (bytes32){
        certificateId++;
        Certificate memory newCertificate = Certificate(certificateId, msg.sender, startTime, endTime, amount);
        // Encoding the certificate to bytes and then hashing it
        bytes32 hash = keccak256(abi.encode(newCertificate.uuid, newCertificate.owner, newCertificate.startTime, newCertificate.endTime, newCertificate.amount));
        certificates[hash] = newCertificate;
        hashAndAmount[hash][amount] = true;
        return hash;
    }

    // function verifyCertificate(uint uuid, address owner, uint256 startTime, uint256 endTime, uint amount) public view returns(bool){
    //     bytes32 hash = keccak256(abi.encode(uuid, owner, startTime, endTime, amount));
    //     if(certificates[hash].owner != address(0)){
    //         return true;
    //     }
    //     return false;
    // }

    // for the regulator
    function verifyCertificateByHashAndAmount(bytes32 hash, uint amount) public view returns(bool){
        if(hashAndAmount[hash][amount] == true){
            return true;
        }
        return false;
    }


    
}