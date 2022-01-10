var DataTypes = artifacts.require("DataTypes");

module.exports = function(deployer) {
    deployer.deploy(DataTypes);
};