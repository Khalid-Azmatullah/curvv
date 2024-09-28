const value = process.env.keyToAll;

if (value) {
    console.log(`The value of 'keyToAll' is: ${value}`);
} else {
    console.log("The environment variable 'keyToAll' is not set.");
}
