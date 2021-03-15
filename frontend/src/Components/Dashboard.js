d import React, { useEffect, useState } from "react";
import { Select } from "antd";
import LineChart from "./LineChart";

const { Option } = Select;

const Dashboard = () => {
  const [companies, setCompanies] = useState([]);
  const [chartData, setChartData] = useState([]);
  const [companyOptions, setCompanyOptions] = useState([]);

  const handleChange = (value) => {
    asyncFetchChartData(value);
  };

  const asyncFetchChartData = (data) => {
    fetch(
      "http://localhost:8000/api/companies/data", {method: 'POST', body : JSON.stringify(data)}
    )
      .then((response) => response.json())
      .then((json) => setChartData(json))
      .catch((error) => {
        console.log("fetch data failed", error);
      });
  };

  const asyncFetchCompanies = () => {
    fetch(
      "http://localhost:8000/api/companies",
    )
      .then((response) => response.json())
      .then((json) => setCompanyOptions(json))
      .catch((error) => {
        console.log("fetch data failed", error);
      });
  };

  useEffect(() => {
    asyncFetchCompanies();
  }, []);

  return (
    <>
      <div className="charts-select-container">
        <span className="chart-header">Trends</span>
        <div className="select-container">
          <Select
            mode="multiple"
            style={{ width: "100%" }}
            placeholder="Select Companies"
            onChange={handleChange}
            optionLabelProp="label"
          >
            {companyOptions.map((key) => {
        return <option key={key} value={key}>
          <div className="demo-option-label-item">{key}</div>
          </option>;
            })}
          </Select>
        </div>
      </div>
      <div>
        <LineChart data={chartData} />
      </div>
    </>
  );
};

export default Dashboard;
