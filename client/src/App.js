import React from 'react';
import { Layout } from 'antd';
import 'antd/dist/antd.css';
// import './index.css';

import EmployeeTable from './components/EmployeeTable';

const { Content } = Layout ;

const App = () => {
  return (
    <Layout className="layout" style={{height: "100vh"}}>
      <Content style={{ padding: '50px 50px' }}>
        <EmployeeTable/>
      </Content>
    </Layout>
  );
}

export default App;
