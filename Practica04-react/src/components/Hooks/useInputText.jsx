import { useState } from "react";

export default function useInput(initialValue, handleError) {
    const [value, setValue] = useState(initialValue);

    const handleChange = (e) => {
        setValue(e.target.value);

    };

    return {
        value: value,
        setValue: setValue,
        onChange: handleChange,
    };
}