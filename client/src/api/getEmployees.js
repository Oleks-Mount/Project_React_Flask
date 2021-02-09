import axios from 'axios';

const getEmployees = async (options) => {
    console.log("sending request");
    try{
        const response = await axios.get(`/get_employee`);   
        console.log("Request was sent");
        return response.data;
    }catch(e){
        console.log(e);
        return(e);
    }
      
}

export default getEmployees;