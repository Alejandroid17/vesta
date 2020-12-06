const recursive = require("recursive-readdir");
const fs = require("fs");
const path = require("path");
var capitalize = require("capitalize");

const ignoreFiles = [
  "__pycache__",
  ".git",
  "*.yml",
  "node_modules",
  "docs",
  ".github",
  ".idea",
  ".vscode",
  "env",
  "locale",
  "package*",
  "docker*",
  "migrations",
  ".gitignore",
  "LICENCE",
  "README.md",
  "CHANGELOG",
  "requirements.txt",
  "manage.py",
  "urls.py",
  "asgi.py",
  "wsgi.py",
  "apps.py",
];

console.log("Init script");

const basePath = ["docs", "modules"];
const currentPath = process.cwd();

const getTitle = (path, isFolder) => {
  let pathSplit = path.split("/");
  let title = capitalize(
    pathSplit[pathSplit.length - (isFolder ? 2 : 1)]
      .replace(".rst", "")
      .replace(/_/g, " ")
  );
  return title;
};

const getHeader = (title) => {
  return title + "\n" + "=".repeat(title.length);
};

recursive(".", ignoreFiles, (err, files) => {
  files.map((item) => {
    let filePath = path.join(
      currentPath,
      ...basePath,
      item.replace("__init__.py", "index.rst").replace(".py", ".rst")
    );

    let folderPath = path.dirname(filePath);

    if (!fs.existsSync(folderPath)) {
      fs.mkdirSync(folderPath, { recursive: true });
      console.info("Folder created:", folderPath);
    }

    if (!fs.existsSync(filePath)) {
      let fileTitle = getTitle(filePath, filePath.includes("index.rst"));
      fs.writeFile(filePath, getHeader(fileTitle), (err) => {
        if (err) throw err;
        console.info("File created:", filePath);
      });
    }
  });
});
