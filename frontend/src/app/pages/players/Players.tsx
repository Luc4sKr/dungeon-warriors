import { BasicTable } from "../../shared/components/basicTable/BasicTable";

import styles from "./Players.module.css";

export const Players = () => {
    return (
        <div>
            <h1 className={styles.title}>Players</h1>

            <div className={styles.tableContainer}>
                <BasicTable />
            </div>
        </div>
    )
}