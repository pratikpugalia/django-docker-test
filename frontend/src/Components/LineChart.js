import React from "react";
import { Line } from "@ant-design/charts";

const LineChart = ({ data }) => {
  console.log(data);
  const config = {
    data: data,
    xField: "month",
    yField: "headcount",
    seriesField: "company",
    point: {
      size: 2.5,
      shape: 'diamond',
    },
    yAxis: {
      label: {
        formatter: function formatter(v) {
          return "".concat(v).replace(/\d{1,3}(?=(\d{3})+$)/g, function (s) {
            return "".concat(s, ",");
          });
        },
      },
    },
    color: ["#1979C9", "#D62A0D", "#FAA219"],
  };

  return <Line {...config} />;
};

export default LineChart;
