import { motion, AnimatePresence } from "framer-motion";
import { useEffect } from "react";
import styles from "../styles/components/loading.module.css";

export default function Loading({ open, children }) {
  useEffect(() => {
    if (open) {
      document.body.style.overflowY = "hidden";
    } else {
      document.body.style.overflowY = "auto";
    }
  }, [open]);
  return (
    <AnimatePresence>
      {open && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className={styles.loading}
        >
          <div className={styles.opacity}></div>
          <motion.div
            className={styles.loader}
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            exit={{ scale: 0 }}
          >
            {children || "Loading..."}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
