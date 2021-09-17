// object literal switch case
function getDrink(type) {
  var drinks = {
    coke: 'Coke',
    pepsi: 'Pepsi',
    lemonade: 'Lemonade',
    default: 'Default item',
  };
  return 'The drink I chose was ' + (drinks[type] || drinks['default']);
}

var drink = getDrink('coke');
// The drink I chose was Coke
console.log(drink);
