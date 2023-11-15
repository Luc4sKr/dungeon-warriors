import { useState, FormEvent, ChangeEvent } from "react"
import { Form, FormDiv, FormWrapper, SelectedImage } from "./Register.style";
import { Button, TextField } from "@mui/material";
import { PlayerRegister } from "../../shared/models/player";
import { register } from "../../shared/services/player_api";

export const Register = () => {
    const [formData, setFormData] = useState<PlayerRegister>({
        username: "",
        email: "",
        password: "",
        image: null,
    });

    const onSubmitForm = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        console.log(formData)

        register(formData);
    }

    const handleInput = (event: ChangeEvent<HTMLInputElement>) => {
        const fieldName = event.target.name;

        setFormData({
            ...formData,
            [fieldName]: event.target.value,
        });
    }

    const handleImage = (event: ChangeEvent<HTMLInputElement>) => {
        const fieldName = event.target.name;
        const files = event.target.files;

        if (files && files.length > 0) {
            const selectedImage = files[0];

            setFormData({
                ...formData,
                [fieldName]: selectedImage,
            });
        }
    };


    return (
        <FormWrapper>
            <Form onSubmit={onSubmitForm}>
                <FormDiv>
                    <h1 style={{ textAlign: "center" }}>Register</h1>
                </FormDiv>

                <FormDiv>
                    <TextField
                        type="text"
                        label="Username"
                        variant="standard"
                        id="username"
                        name="username"
                        value={formData.username}
                        onChange={handleInput}
                    />
                </FormDiv>

                <FormDiv>
                    <TextField
                        type="email"
                        label="Email"
                        variant="standard"
                        id="email"
                        name="email"
                        value={formData.email}
                        onChange={handleInput}
                    />
                </FormDiv>

                <FormDiv>
                    <TextField
                        type="password"
                        label="Password"
                        variant="standard"
                        id="password"
                        name="password"
                        value={formData.password}
                        onChange={handleInput}
                    />
                </FormDiv>

                <FormDiv>
                    <Button
                        variant="contained"
                        component="label"
                    >
                        Upload Profile Image
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

                    {formData.image && (
                        <SelectedImage>
                            <p style={{ color: "rgba(0, 0, 0, 0.6)" }}>Selected Image:</p>
                            <img
                                src={URL.createObjectURL(formData.image)}
                                alt="Selected"
                                style={{ width: "100%" }}
                            />
                        </SelectedImage>
                    )}
                </FormDiv>

                <FormDiv>
                    <Button
                        type="submit"
                        variant="contained"
                    >
                        Send
                    </Button>
                </FormDiv>
            </Form>
        </FormWrapper>
    )
}