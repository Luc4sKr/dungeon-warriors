import { ButtonHTMLAttributes, ReactNode, ReactElement, cloneElement } from "react"

import "./Button.css"

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
    children: ReactNode;
    icon?: ReactElement;
    variant?: "default" | "transparent" | "submit" | "cancel";
}

export const Button = (props: ButtonProps) => {
    const { variant } = props;

    switch (variant) {
        case "transparent":
            return <TransparentButton {...props} />
        default:
            return <DefaultButton {...props} />
    }
}

export const DefaultButton = (props: ButtonProps) => {
    const { children, icon } = props; 

    return (
        <button {...props} className="button default-button">
            <span>
                {children}
            </span>
            {icon && cloneElement(icon, { className: "icon" })}
        </button>
    )
}

// para depis
export const TransparentButton = () => {
    return <button>teste</button>
}