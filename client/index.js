const { join } = require("node:path");
const { Socket } = require("node:net");
const { createReadStream } = require("node:fs");
const { app, Tray, Menu } = require("electron");
const { watch } = require("chokidar");
const config = require("./config.js");

if (!app.requestSingleInstanceLock()) {
  return app.quit();
}

app.setLoginItemSettings({
  openAtLogin: true,
});

app.whenReady().then(() => {
  console.log(`App ready (${process.pid})`);

  // These are all of the menu options that show up when you click the app
  // icon in the bottom right system tray on windows.
  let menu = Menu.buildFromTemplate([
    {
      label: "Exit",
      click: () => {
        app.quit();
      },
    },
  ]);

  let icon;
  let iconPath = join(__dirname, "icon.png");

  icon = new Tray(iconPath);
  icon.setToolTip("Oculus");
  icon.setContextMenu(menu);

  // Chokidar globs require unix-style paths.
  // e.x. C:\Users\Ethan Anders\Documents\Warcraft III\BattleNet\**
  //   -> C:/Users/Ethan Anders/Documents/Warcraft III/BattleNet/**
  const paths = config.watch.map((path) => path.replace(/\\/g, "/"));
  const watcher = watch(paths);

  watcher.on("ready", () => {
    console.log("Watching directories:");
    paths.forEach((path) => console.log(`  ${path}`));

    watcher.on("add", upload);
    watcher.on("change", upload);
  });
});

function upload(path) {
  console.log(`Uploading replay: ${path}`);

  const socket = new Socket();

  socket.connect(config.server.port, config.server.host, () => {
    const stream = createReadStream(path).pipe(socket);

    socket.on("data", (data) => {
      console.log("" + data);
    });

    stream.on("error", (e) => {
      console.error(e);
    });

    stream.on("close", () => {
      console.log(`Uploaded: ${path}`);
      socket.destroy();
    });
  });
}
