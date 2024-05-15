// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract CO2EmissionCertificate {
    bytes32 public computedHash;
    constructor(bytes32 _computedHash) {
        computedHash = _computedHash;
    }
}

contract CO2EmissionCertificateFactory {
    address owner;
    uint public certificateCount;
    mapping (uint => CO2EmissionCertificate) public certificates;
    constructor () {
        owner = msg.sender;
    }
    // Events
    event CertificateEvent(CO2EmissionCertificate certificate);

    // Modifiers
    modifier onlyOwner() {
        require(owner == msg.sender, "Only the owner can call this method");
        _;
    }

    function createCertificate(bytes32 _computedHash) public onlyOwner returns(uint certificateId) {
        CO2EmissionCertificate certificate = new CO2EmissionCertificate(_computedHash);
        emit CertificateEvent(certificate);
        certificates[certificateCount] = certificate;
        certificateId = certificateCount; // Set return to certificate id used
        certificateCount++;
    }

    // Will be removed, used for testing purposes only
    function hashCertificateData(address recipient, uint startTime, uint endTime, uint amount) public pure returns(bytes32) {
        require(startTime < endTime, "Start time must be before end time");
        require(amount > 0, "Amount must be positive");
        return keccak256(abi.encodePacked(recipient, startTime, endTime, amount));
    }

}
