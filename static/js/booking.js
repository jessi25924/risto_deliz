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
