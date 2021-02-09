import React, { useState } from 'react';
import { Layout, Table, Tag, Space } from 'antd';

import getEmployees from '../api/getEmployees';

const { Content } = Layout;

const columns = [
  // {
    // title: 'Index',
    // dataIndex: 'key',
    // key: 'key',
  // },
  {
    title: 'Name',
    dataIndex: 'name',
    key: 'name'
  },
  {
    title: 'Age',
    dataIndex: 'age',
    key: 'age',
  },

  {
    title: 'Job',
    key: 'Job',
    dataIndex: 'job',
    render: job => {
      let color;
      switch (job.toLowerCase()) {
        case "developer":
          color = 'geekblue';
          break;
        case "teacher":
          color = 'volcano';
          break;
        default:
          color = 'green';
      }
      return ( 
        <Tag color = {color} key = {job}> 
        {job.toUpperCase()}
        </Tag>
      );
    }
  }
];

const dataForTable = [
  {
    key: '1',
    name: 'Andrew Andreev',
    age: 35,
    address: 'New York No. 1 Lake Park',
    job: 'developer',
  },
  {
    key: '2',
    name: 'John Johnson',
    age: 25,
    address: 'London No. 1 Lake Park',
    job: 'doctor',
  },
  {
    key: '3',
    name: 'Ivan Ivanov',
    age: 40,
    address: 'Sidney No. 1 Lake Park',
    job: 'teacher',
  },
];

class EmployeeTable extends React.Component {
  async getData(){
    let data = await getEmployees();
    console.log(data);
    return data;
  }

  constructor(props) {
    super(props);
    this.setState({
        tableData: [],
        isLoading: true
    });
  }

  componentWillMount(){
    this.setState({
        tableData: [],
        isLoading: true
    });
  }
  
  async componentDidMount(){
    // let data = this.getData();
    // if(data.length == 0){
    // 
    // }
    let { workers } = await this.getData();
    
    console.log("component did mount")
    this.setState({
      tableData: workers.length > 0 ? workers : [],
      isLoading: false
  });
  }
  
  render() {
    const loading = this.state.isLoading;
    const data = this.state.tableData;

    console.log(this.state);
    return ( 
      <Table dataSource = {data} columns ={columns} loading={loading}/> 
    );
  };
}

export default EmployeeTable;