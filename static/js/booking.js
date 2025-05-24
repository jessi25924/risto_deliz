/**
 * Handles automatic URL parameter updates based on selected date and time.
 * This script listens for changes in the date input and table selected fields.
 * Used for dynamically filtering available booking times on the server side
 * by responding to the updated query parameters.
 *
 * Elments:
 *  - id_date: html input element of the type "date"
 *  - id_table: html select element for choosing a table
 */

document.addEventListener("DOMContentLoaded", function () {
  const dateInput = document.getElementById("id_date");
  const tableSelect = document.getElementById("id_table");

  function reloadWithParams() {
    const date = dateInput.value;
    const table = tableSelect.value;
    if (date && table) {
      window.location.search = `?date=${date}&table=${table}`;
    }
  }

  dateInput.addEventListener("change", reloadWithParams);
  tableSelect.addEventListener("change", reloadWithParams);
});
