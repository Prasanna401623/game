// Google Apps Script Web App backend for Loops playtime telemetry.
// This is pasted into the Apps Script editor, not run by Ren'Py directly.
//
// Setup:
// 1. Create a Google Sheet (any name).
// 2. Open that Sheet's URL: https://docs.google.com/spreadsheets/d/<SHEET_ID>/edit
//    Copy the <SHEET_ID> part and paste it into SHEET_ID below.
// 3. Extensions > Apps Script, delete the placeholder code, paste this file in.
// 4. Deploy > New deployment > type "Web app".
//    - Execute as: Me
//    - Who has access: Anyone
// 5. Copy the deployed /exec URL into TELEMETRY_URL in Story/Telemetry/telemetry.rpy.
// 6. Any time you edit this file, Deploy > Manage deployments > edit (pencil)
//    > New version > Deploy, editing alone does not update the live URL.

const SHEET_ID = "PASTE_YOUR_SHEET_ID_HERE";
const SHEET_NAME = "events";

function doPost(e) {
  const sheet = getSheet_();
  const data = JSON.parse(e.postData.contents);

  sheet.appendRow([
    new Date(),
    data.code || "",
    data.event || "",
    data.scene || "",
    data.elapsed_seconds || 0,
    !!data.completed,
  ]);

  return ContentService.createTextOutput("ok");
}

function getSheet_() {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    sheet.appendRow(["timestamp", "code", "event", "scene", "elapsed_seconds", "completed"]);
  }
  return sheet;
}
