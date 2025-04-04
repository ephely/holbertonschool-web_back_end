export default function createEmployeesObject(departmentName, employees) {
  const new_employee = {
    [departmentName]: employees,
  };
  return new_employee;
}
