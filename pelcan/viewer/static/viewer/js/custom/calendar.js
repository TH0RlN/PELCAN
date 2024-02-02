function clearCalendar(calendar) {
    calendar.clearEvents();
    holidays = calendar.getHolidays();
    for (holiday of holidays) {
        calendar.removeHolidays([holiday.title], true, true);
    }
}

function main() {
    var calendarInstance = new calendarJs("calendar", {
        manualEditingEnabled: true
        // All your options can be set here
    });

    clearCalendar(calendarInstance);
}

main();