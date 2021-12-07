const Migrations = artifacts.require("Migrations");
const HiWorld = artifacts.require("HiWorld");

module.exports = function (deployer) {
  deployer.deploy(Migrations);
  deployer.deploy(HiWorld);
};
