function pizzaOven(crustType,sauceType,cheeses,toppings) {
    var pizza = {} ;
    pizza.crustType = crustType ;
    pizza.sauceType=sauceType;
    pizza.cheeses=cheeses;
    pizza.toppings=toppings;
    return pizza 

}
var pizzaType = pizzaOven("deep dish","traditional",["mozzarella","pepperoni","sausage"])
console.log("pizzaType") ;


// random pizza



typePizza=["mozarella","soySauce","pepper","pepperoni"],["sausage","tomato","feta","pest"]
function randomPizza(typePizza) {
var randomnum = math.random ;
number = number*typePizza.length
var int = math.floor(number)
    return typePizza[int] ;
}


