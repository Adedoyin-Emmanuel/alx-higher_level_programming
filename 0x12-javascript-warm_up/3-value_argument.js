#!/usr/bin/node
/* 
    A script that prints the first argument passed to it
*/
const firstArgument = process.argv[3];
if(!firstArgument){
    console.log('No argument');
}else{
    console.log(firstArgument);
}
