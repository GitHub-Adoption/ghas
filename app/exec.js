const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  readline.question('Enter your command: ', (userInput) => {
    eval(userInput); // This is a security risk
    readline.close();
  });