function createSpreadsheetTrigger(){
    // 스프레드 시트 파일에 새 데이터가 추가될 때마다 실행되는 trigger 생성
    // 한번만 실행하면 됩니다.
    sheet = SpreadsheetApp.openById('trigger를 걸 spreadsheet 파일 id');
    ScriptApp.newTrigger('trigger 실행과 동시에 실행될 함수명').forSpreadsheet(sheet).onChange().create();
    // ScriptApp.newTrigger('myFunction').forSpreadsheet(sheet).onChange().create();
}

function myFunction() {
    // do something
}