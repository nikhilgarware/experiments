let dataToSend = [];
let plantId = 1;
function generateReport(reportType) {
  switch (reportType) {
    case 'measured_data':
      dataToSend.push([{ name: 'Nikhil', plantId: plantId }]);
      console.log(dataToSend);

      break;
    case 'plant_data':
      break;
    default:
      break;
  }
}
generateReport('measured_data');
