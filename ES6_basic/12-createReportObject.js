export default function createReportObject(employeesList) {
    const rep_obj = { allEmployees: { ...employeesList } };
    getNumberOfDepartments() {
        Object.keys(allEmployees).length
    };
    return rep_obj
}
