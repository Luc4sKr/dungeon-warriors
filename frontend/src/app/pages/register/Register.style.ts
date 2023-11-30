import styled from 'styled-components';
import "/public/css/global.css";

export const FormWrapper = styled.div`
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	margin: 30px 0;
`;

export const Form = styled.form`
	background-color: var(--form-color);
	width: 500px;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
`;

export const FormDiv = styled.div`
	width: 100%;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	margin: 20px 0;

	& > * {
    	width: 90%;
  	}
`;

export const FormLabel = styled.label`
	font-size: 18px;
	color: #fff;
`;

export const SelectedImage = styled.div`
	width: 80%;
	margin: 10px auto;
	display: flex;
	flex-direction: column;
	align-items: center;
`;
