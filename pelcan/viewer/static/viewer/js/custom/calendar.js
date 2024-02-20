function clearCalendar(calendar) {
    calendar.clearEvents();
    holidays = calendar.getHolidays();
    for (holiday of holidays) {
        calendar.removeHolidays([holiday.title], true, true);
    }
}

function main(citas, __TRANSLATION_OPTIONS) {
    OPTIONS = __TRANSLATION_OPTIONS;
    OPTIONS['stText'] = ' '
    OPTIONS['ndText'] = ' '
    OPTIONS['rdText'] = ' '
    OPTIONS['thText'] = ' '
    OPTIONS['manualEditingEnabled'] = false;
    var calendarInstance = new calendarJs("calendar", OPTIONS);
    clearCalendar(calendarInstance);
    
    for (cita of citas) {
        calendarInstance.addEvent(cita);
    }
}