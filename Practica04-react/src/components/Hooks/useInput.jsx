import { useState } from "react";

export default function useInput(initialValue, { errorMsg, validator, isCheckbox = false }) {
    const [value, setValue] = useState(initialValue);
    const [error, setError] = useState('');


    const handleChange = (e) => {
        const value = isCheckbox ? e.target.checked : e.target.value;
        setValue(value)
        const isValid = validator(value);
        if (!isValid) {
            setError(errorMsg);
        } else {
            setError('');
        }
    };

    return {
        value,
        setValue,
        onChange: handleChange,
        error,
        setError
    };
}