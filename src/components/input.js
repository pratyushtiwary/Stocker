import styles from "../styles/components/input.module.css";
import React from "react";

export default function Input({
  label,
  actionText,
  id,
  type,
  className,
  required,
  onSubmit,
  value,
  onChange,
}) {
  const [float, setFloat] = React.useState(false);

  function handleFocus(e) {
    setFloat(true);
  }

  function handleBlur(e) {
    if (e.currentTarget.value.replace(" ", "") === "") {
      setFloat(false);
    }
  }

  function handleSubmit(e) {
    e.preventDefault();
    onSubmit(e);
  }

  return (
    <form className={styles.input + " " + className} onSubmit={handleSubmit}>
      <label htmlFor={id} className={float && styles.float}>
        {label}
      </label>
      <input
        type={type}
        id={id}
        value={value}
        onChange={onChange}
        onFocus={handleFocus}
        onBlur={handleBlur}
        required={required}
      />
      <button type="submit">{actionText}</button>
    </form>
  );
}
