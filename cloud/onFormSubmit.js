function onFormSubmit(event) {
  
  record_array      = []

  var form          = FormApp.openById('1JyzKyfPOmUgF9DuNHL_XgraopTz-oEOScwmX54EVf1g'); // Form ID
  var formResponses = form.getResponses();                                              
  var formCount     = formResponses.length;                                             

  var formResponse  = formResponses[formCount - 1];                                     // Taking the last repsone and get the items from that respon
  var itemResponses = formResponse.getItemResponses();                                 

  for (var i = 0; i < itemResponses.length; i++){                                       // Loop through the response
    var title       = itemResponses[i].getItem().getTitle();
    var answer      = itemResponses[i].getResponse();

    Logger.log(title);
    Logger.log(answer);

    record_array.push(answer);
  }

  AddRecord(record_array[0], record_array[1]);                                           // Add the data to a new row.

}

function AddRecord(name, email){
  var url           = 'https://docs.google.com/spreadsheets/d/1aOQRmc_mDPXV7kXcOEDsUV9mowN7tM6UTR0n8eIlZAI/edit#gid=0';  // URL of google sheet
  var ss            = SpreadsheetApp.openByUrl(url);
  var dataSheet     = ss.getSheetByName("Sheet1");
  dataSheet.appendRow([name, email, new Date()]);
}
