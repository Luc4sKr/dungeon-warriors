import { useState, FormEvent, ChangeEvent } from "react"
import { Form, FormDiv } from "./Register.style";

export const Register = () => {
    const [image, setImage] = useState<File | null>(null);

    const uploadImage = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        if (!image) {
            alert('Por favor, selecione uma imagem antes de enviar.');
            return;
        }

        console.log("imagem")
    }

    const handleImageChange = (event: ChangeEvent<HTMLInputElement>) => {
        const files = event.target.files;

        if (files && files.length > 0) {
            const selectedImage = files[0];
            setImage(selectedImage);
        }
    };

    return (
        <Form onSubmit={uploadImage}>
            <FormDiv>
                <label htmlFor="image">Imagem: </label>
                <input
                    type='file'
                    id='image'
                    name='image'
                    onChange={handleImageChange}
                    accept='image/*'
                    key={Math.random()}
                />

                {image && (
                    <div>
                        <p>Selected Image:</p>
                        <img
                            src={URL.createObjectURL(image)}
                            alt="Selected"
                            style={{ maxWidth: '100px' }}
                        />
                    </div>
                )}
            </FormDiv>

            <button type='submit'>Salvar</button>
        </Form>
    )
}