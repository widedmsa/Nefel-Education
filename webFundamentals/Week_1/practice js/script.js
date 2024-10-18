function nameElements(elementName) {
    console.log(elementName);
}

function turnOff(element) {
    element.innerText = "Off";
    if (element.innerText === "Off"){
        element.style.backgroundColor = "red";
        
    }
    else {
        
        element.innerText="On";
    }
}
// hide function 
function hide(element){
    element.remove() ;
}
// over and out functions 
function over(element){
    element.style.backgroundColor=  "red" ;
}
function out(this){
    element.style.backgroubndColor="blue" ;
}