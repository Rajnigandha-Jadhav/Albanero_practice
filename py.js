const weak = require('weak');

// // create an object
// const myObject = {
//   name:"abc"
// };

// // create a weak reference to the object
// const myWeakRef = weak(myObject);

// // print the weak reference
// console.log(myWeakRef);

// // remove the original object from memory
// myObject = null;

// // check if the weak reference is still valid
// console.log(weak.get(myWeakRef)); // should return undefined
let obj = {foo: 'bar'};
let ref = weak(obj, () => {
  console.log('Object has been garbage collected');
});
