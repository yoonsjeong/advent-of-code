class FileNode {
    constructor(name, size) {
        this.size = parseInt(size);
        this.name = name;
    }
}

class DirectoryNode {
    constructor(name, parent) {
        this.name = name;
        this.children = []
        this.parent = parent;
    }

    getReferenceOfChild(childName) {
        let index = this.children.findIndex(child => {
            return child.name == childName;
        });
        return this.children[index]
    }

    getParent() {
        return this.parent
    }

    addChild(childToAdd) {
        /* only add child if it cannot be found already */
        let attemptSearch = this.children.findIndex(child => {
            return childToAdd.name == child.name;
        })
        if (-1 == attemptSearch)
            this.children.push(childToAdd);
    }

    getSize() {
        let totalSize = 0;
        for (let child of this.children)
        {
            if (child instanceof FileNode)
                totalSize += child.size;
            else if (child instanceof DirectoryNode)
                totalSize += child.getSize();
        }
        return totalSize;
    }
}

var executeLs = (currentReference, commandChunk) => {
    for (let line of commandChunk.split("\r\n").slice(1))
    {
        if (line.startsWith("dir"))
        {
            let directoryName = line.split(" ")[1];
            currentReference.addChild(new DirectoryNode(directoryName, currentReference));
        }
        else
        {
            let [_, fileSize, fileName] = line.match(/(\d+) ([^\s]+)/);
            currentReference.addChild(new FileNode(fileName, fileSize));
        }
    }
}

var executeCd = (currentReference, commandChunk) => {
    let directoryName = commandChunk.split(" ")[1];
    if (directoryName == "..")
        return currentReference.getParent();
    
    currentReference.addChild(new DirectoryNode(directoryName, currentReference));
    return currentReference.getReferenceOfChild(directoryName);
}

var getDirectoriesUnderSize = (node, maxSize) => {
    if (node === null) return [];
    let directories = [];

    if (node instanceof DirectoryNode)
    {
        if (node.getSize() <= maxSize)
            directories.push(node);
        for (let child of node.children)
            directories = directories.concat(getDirectoriesUnderSize(child, maxSize));
    }
    return directories;
}

var getDirectoriesOverSize = (node, minSize) => {
    if (node === null) return [];
    let directories = [];

    if (node instanceof DirectoryNode)
    {
        if (node.getSize() >= minSize)
            directories.push(node);
        for (let child of node.children)
            directories = directories.concat(getDirectoriesOverSize(child, minSize));
    }
    return directories;
}

var part1 = (commandList) => {
    let rootNode = new DirectoryNode("/", null);
    let currentReference = rootNode;
    for (let commandChunk of commandList)
    {
        if (commandChunk.startsWith("cd"))
            currentReference = executeCd(currentReference, commandChunk)
        else if (commandChunk.startsWith("ls"))
            executeLs(currentReference, commandChunk)
    }

    let totalSize = 0;
    let criteriaDirs = getDirectoriesUnderSize(rootNode, 100000);
    for (let dir of criteriaDirs)
    {
        totalSize += dir.getSize()
    }
    return totalSize;
}

var part2 = (commandList) => {
    let rootNode = new DirectoryNode("/", null);
    let currentReference = rootNode;
    for (let commandChunk of commandList)
    {
        if (commandChunk.startsWith("cd"))
            currentReference = executeCd(currentReference, commandChunk)
        else if (commandChunk.startsWith("ls"))
            executeLs(currentReference, commandChunk)
    }

    let criteriaSize = 70000000 - rootNode.getSize();
    criteriaSize = 30000000 - criteriaSize;
    let criteriaDirs = getDirectoriesOverSize(rootNode, criteriaSize);
    let minimumSize = 30000000;
    for (let dir of criteriaDirs)
    {
        let currSize = dir.getSize();
        if (currSize < minimumSize)
            minimumSize = currSize;
    }
    return minimumSize;
}

var main = (input) => {
    let commandList = input.split("\r\n$ ").slice(1);
    let p1 = part1(commandList);
    let p2 = part2(commandList);

    console.log(`The answer to part 1 is: ${p1}`);
    console.log(`The answer to part 2 is: ${p2}`);
}

/* parse and enter */
require("fs").readFile("day-07.txt", "utf8", (err, data) => {
    err && console.error(err);
    main(data);
})
