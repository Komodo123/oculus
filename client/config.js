const { app } = require("electron");
const home = app.getPath("home");

const config = {
  watch: [
    `${home}/Documents/Warcraft III/BattleNet/**/*.w3g`,
    `!${home}/Documents/Warcraft III/BattleNet/**/TempReplay.w3g`,
  ],
};

if (app.isPackaged) {
  config.server = {};
} else {
  config.server = {
    host: "127.0.0.1",
    port: 8080,
  };

  config.watch.push(__dirname + "/LastReplay.w3g");
}

module.exports = config;
