import { useState, FormEvent, ChangeEvent } from "react"
import { Form, FormDiv, FormWrapper, FormLabel, SelectedImage } from "./Register.style";
import { Button, TextField } from "@mui/material";

interface FormData {
    username: string;
    email: string;
    password: string;
    image: File | null;
}

export const Register = () => {
    const [formData, setFormData] = useState<FormData>({
        username: "",
        email: "",
        password: "",
        image: null,
    });

    const [image, setImage] = useState<File | null>(null);

    const onSubmitForm = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        console.log(formData)
    }

    const handleUsername = (event: ChangeEvent<HTMLInputElement>) => {
        console.log(event)
        const fieldName = event.target.name;
        
        setFormData({
            ...formData,
            [fieldName]: event.target.value,
        });

        console.log(fieldName)
    }

    const handleImage = (event: ChangeEvent<HTMLInputElement>) => {
        const files = event.target.files;

        if (files && files.length > 0) {
            const selectedImage = files[0];
            setImage(selectedImage);
        }
    };


    return (
        <FormWrapper>
            <Form onSubmit={onSubmitForm}>
                <FormDiv>
                    <TextField
                        type="text"
                        label="Username"
                        variant="standard"
                        id="username"
                        name="username"
                        value={formData.username}
                        onChange={handleUsername}
                    />
                </FormDiv>

                <FormDiv>
                    <Button
                        variant="contained"
                        component="label"
                    >
                        Upload File
                        <input
                            type='file'
                            id='image'
                            name='image'
                            onChange={handleImage}
                            accept='image/*'
                            key={Math.random()}
                            hidden
                        />
                    </Button>

                    {image && (
                        <SelectedImage>
                            <p>Selected Image:</p>
                            <img
                                src={URL.createObjectURL(image)}
                                alt="Selected"
                                style={{ width: "100%" }}
                            />
                        </SelectedImage>
                    )}
                </FormDiv>

                <button type='submit'>Salvar</button>
            </Form>
        </FormWrapper>
    )
}