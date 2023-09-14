// Add your JavaScript code here to highlight the current month's dates
function generateCalendar(year, month) {
    const calendarBody = document.getElementById('calendar-body');
    const currentMonthHeading = document.getElementById('current-month');

    calendarBody.innerHTML = '';

    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const firstDay = new Date(year, month, 1).getDay();

    currentMonthHeading.textContent = new Date(year, month, 1).toLocaleString('default', { month: 'long', year: 'numeric' });

    let dayCounter = 1;

    for (let i = 0; i < 6; i++) {
        const row = document.createElement('tr');

        for (let j = 0; j < 7; j++) {
            const cell = document.createElement('td');

            if ((i === 0 && j < firstDay) || dayCounter > daysInMonth) {
                cell.textContent = '';
            } else {
                const currentDate = new Date();
                const currentYear = currentDate.getFullYear();
                const currentMonth = currentDate.getMonth();
                const currentDateValue = currentDate.getDate();
                const cellDate = new Date(year, month, dayCounter);

                cell.textContent = dayCounter;
                cell.dataset.date = cellDate.toISOString();

                if (
                    cellDate.getFullYear() === currentYear &&
                    cellDate.getMonth() === currentMonth &&
                    dayCounter === currentDateValue
                ) {
                    cell.classList.add('current-date');
                }

                dayCounter++;
            }

            row.appendChild(cell);
        }

        calendarBody.appendChild(row);
    }
}

const currentDate = new Date();
const currentYear = currentDate.getFullYear();
const currentMonth = currentDate.getMonth();
const currentDay = currentDate.getDate();

generateCalendar(currentYear, currentMonth);

const today = new Date(currentYear, currentMonth, currentDay);

document.getElementById('today-date-input').value = today.toISOString();
