import styles from "../styles/components/header.module.css";
import React from "react";

export default function Header() {
  return (
    <div className={styles.header}>
      <div className={styles.titleLogo}>
        <div className={styles.logo}></div>
        <h1 className={styles.title}>Stocker</h1>
      </div>
    </div>
  );
}
