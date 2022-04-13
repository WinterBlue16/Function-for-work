function getSheetsData() {
    allSheets = SpreadsheetApp.openById('spread sheet 파일 id').getSheets();

    for (sheet of allSheets) {
        // sheet는 스프레드 시트의 하단 탭을 말합니다. 
        // 해당 스프레드 시트의 모든 데이터를 탭 단위로 보여줍니다. 
        // row 데이터 하나가 object 형태로 array에 담겨 출력됩니다. 
        let data = sheet.getDataRange().getValues();
        console.log(data);
    }
}