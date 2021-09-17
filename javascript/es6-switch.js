let pinCode = [
  411038,
  411039,
  411040,
  41102,
  411056,
  411025,
  532145,
  65248,
  687452,
  965344,
];
let city;
const selectedPinCode = pinCode[Math.floor(Math.random() * 10)];
switch (selectedPinCode) {
  case String(selectedPinCode).startsWith('4'):
    city = 'Pune City';
    return 'Pune City';

  default:
    city = 'Mumbai city';
    return 'Mumbai City';
}
