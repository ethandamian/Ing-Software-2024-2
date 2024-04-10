export const isOnlyLettersAndSpace = (value) => {
    return /^[a-zA-ZñÑ\s|]+$/.test(value);
}