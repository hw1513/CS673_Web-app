-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 03, 2019 at 05:06 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `authenticate_friend`
--

CREATE TABLE `authenticate_friend` (
  `id` int(11) NOT NULL,
  `current_user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `authenticate_friend`
--

INSERT INTO `authenticate_friend` (`id`, `current_user_id`) VALUES
(2, 1),
(1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `authenticate_friend_users`
--

CREATE TABLE `authenticate_friend_users` (
  `id` int(11) NOT NULL,
  `friend_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `authenticate_friend_users`
--

INSERT INTO `authenticate_friend_users` (`id`, `friend_id`, `user_id`) VALUES
(3, 1, 2),
(4, 1, 3),
(2, 2, 3);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add chat message', 1, 'add_chatmessage'),
(2, 'Can change chat message', 1, 'change_chatmessage'),
(3, 'Can delete chat message', 1, 'delete_chatmessage'),
(4, 'Can view chat message', 1, 'view_chatmessage'),
(5, 'Can add thread', 2, 'add_thread'),
(6, 'Can change thread', 2, 'change_thread'),
(7, 'Can delete thread', 2, 'delete_thread'),
(8, 'Can view thread', 2, 'view_thread'),
(9, 'Can add log entry', 3, 'add_logentry'),
(10, 'Can change log entry', 3, 'change_logentry'),
(11, 'Can delete log entry', 3, 'delete_logentry'),
(12, 'Can view log entry', 3, 'view_logentry'),
(13, 'Can add permission', 4, 'add_permission'),
(14, 'Can change permission', 4, 'change_permission'),
(15, 'Can delete permission', 4, 'delete_permission'),
(16, 'Can view permission', 4, 'view_permission'),
(17, 'Can add group', 5, 'add_group'),
(18, 'Can change group', 5, 'change_group'),
(19, 'Can delete group', 5, 'delete_group'),
(20, 'Can view group', 5, 'view_group'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add content type', 7, 'add_contenttype'),
(26, 'Can change content type', 7, 'change_contenttype'),
(27, 'Can delete content type', 7, 'delete_contenttype'),
(28, 'Can view content type', 7, 'view_contenttype'),
(29, 'Can add session', 8, 'add_session'),
(30, 'Can change session', 8, 'change_session'),
(31, 'Can delete session', 8, 'delete_session'),
(32, 'Can view session', 8, 'view_session'),
(33, 'Can add friend', 9, 'add_friend'),
(34, 'Can change friend', 9, 'change_friend'),
(35, 'Can delete friend', 9, 'delete_friend'),
(36, 'Can view friend', 9, 'view_friend'),
(37, 'Can add programs', 10, 'add_programs'),
(38, 'Can change programs', 10, 'change_programs'),
(39, 'Can delete programs', 10, 'delete_programs'),
(40, 'Can view programs', 10, 'view_programs'),
(41, 'Can add list', 11, 'add_list'),
(42, 'Can change list', 11, 'change_list'),
(43, 'Can delete list', 11, 'delete_list'),
(44, 'Can view list', 11, 'view_list');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$120000$HmgXkYrlxAQg$H0MHtmgTrkFBSHMjdN/hIGzmpJZO1t7lCgZthnT68us=', '2019-04-03 04:16:57.388049', 0, 'hw1513', 'Huaiqian', 'Wu', 'huaiqianwu001@outlook.com', 0, 1, '2019-03-28 04:21:35.490389'),
(2, 'pbkdf2_sha256$120000$xN4pfBxDgjAw$dQ8j7bOgl4zItLlvXoEBfHiNE3ORjChTubKWAym3iHs=', '2019-04-03 04:16:44.701612', 1, 'admin', '', '', 'hw1513@bu.edu', 1, 1, '2019-03-28 05:02:05.323430'),
(3, 'pbkdf2_sha256$120000$ZFAgSfhVqdJs$jLlHjQohX0xUXTWboAIfraTT8b08POJkCw/BaJiKPeY=', '2019-03-28 20:49:58.536844', 0, 'luomucheng', 'mucheng', 'luo', 'hw1513@bu.edu', 0, 1, '2019-03-28 14:20:04.323978');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `chat_chatmessage`
--

CREATE TABLE `chat_chatmessage` (
  `id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `thread_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `chat_chatmessage`
--

INSERT INTO `chat_chatmessage` (`id`, `message`, `timestamp`, `thread_id`, `user_id`) VALUES
(66, 'Hello, Is that hw1513?', '2019-04-02 23:34:47.437363', 5, 2),
(67, 'This, I am', '2019-04-02 23:35:55.917219', 5, 1),
(68, 'Yes, I am', '2019-04-02 23:36:01.637351', 5, 1),
(69, 'Is that Luomu Cheng', '2019-04-03 04:00:20.325416', 4, 1),
(70, 'hi, i shi da sha bi', '2019-04-03 04:17:24.190099', 5, 2),
(71, 'gun', '2019-04-03 04:17:29.634171', 5, 1),
(72, '?', '2019-04-03 04:17:33.964198', 5, 1),
(73, 'a', '2019-04-03 14:47:09.159834', 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `chat_thread`
--

CREATE TABLE `chat_thread` (
  `id` int(11) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `first_id` int(11) NOT NULL,
  `second_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `chat_thread`
--

INSERT INTO `chat_thread` (`id`, `updated`, `timestamp`, `first_id`, `second_id`) VALUES
(3, '2019-03-28 23:41:05.196070', '2019-03-28 15:33:07.329432', 2, 3),
(4, '2019-03-28 19:03:51.122347', '2019-03-28 19:03:51.122347', 3, 1),
(5, '2019-03-28 19:45:32.299970', '2019-03-28 19:45:32.299970', 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2019-03-28 05:03:54.404911', '1', 'Thread object (1)', 1, '[{\"added\": {}}]', 2, 2),
(2, '2019-03-28 05:04:30.299750', '1', 'Thread object (1)', 2, '[{\"added\": {\"name\": \"chat message\", \"object\": \"ChatMessage object (1)\"}}]', 2, 2),
(3, '2019-03-28 15:32:42.741418', '2', 'Thread object (2)', 3, '', 2, 2),
(4, '2019-03-28 15:32:42.780212', '1', 'Thread object (1)', 3, '', 2, 2),
(5, '2019-03-28 23:41:05.960094', '3', 'Thread object (3)', 2, '[{\"deleted\": {\"name\": \"chat message\", \"object\": \"ChatMessage object (None)\"}}, {\"deleted\": {\"name\": \"chat message\", \"object\": \"ChatMessage object (None)\"}}, {\"deleted\": {\"name\": \"chat message\", \"object\": \"ChatMessage object (None)\"}}, {\"deleted\": {\"name\": \"chat message\", \"object\": \"ChatMessage object (None)\"}}, {\"deleted\": {\"name\": \"chat message\", \"object\": \"ChatMessage object (None)\"}}, {\"deleted\": {\"name\": \"chat message\", \"object\": \"ChatMessage object (None)\"}}]', 2, 2),
(6, '2019-04-02 23:13:59.625032', '1', 'CS673_WebApplication', 1, '[{\"added\": {}}]', 10, 2),
(7, '2019-04-02 23:15:53.977518', '2', 'CS579', 1, '[{\"added\": {}}]', 10, 2),
(8, '2019-04-02 23:16:21.010368', '3', 'CS100', 1, '[{\"added\": {}}]', 10, 2),
(9, '2019-04-02 23:17:31.104041', '1', 'CHAT ROOM | False', 1, '[{\"added\": {}}]', 11, 2),
(10, '2019-04-02 23:20:40.861924', '1', 'Friend object (1)', 1, '[{\"added\": {}}]', 9, 2),
(11, '2019-04-02 23:21:03.929015', '2', 'Friend object (2)', 1, '[{\"added\": {}}]', 9, 2),
(12, '2019-04-02 23:27:53.750827', '3', 'CS100', 2, '[{\"changed\": {\"fields\": [\"project_members\"]}}]', 10, 2),
(13, '2019-04-02 23:27:57.579832', '3', 'CS100', 2, '[{\"changed\": {\"fields\": [\"project_members\"]}}]', 10, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(3, 'admin', 'logentry'),
(5, 'auth', 'group'),
(4, 'auth', 'permission'),
(6, 'auth', 'user'),
(9, 'authenticate', 'friend'),
(1, 'chat', 'chatmessage'),
(2, 'chat', 'thread'),
(7, 'contenttypes', 'contenttype'),
(10, 'programs', 'programs'),
(8, 'sessions', 'session'),
(11, 'todo_list', 'list');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-03-28 04:19:59.398336'),
(2, 'auth', '0001_initial', '2019-03-28 04:20:02.364624'),
(3, 'admin', '0001_initial', '2019-03-28 04:20:03.508682'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-03-28 04:20:03.532668'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-03-28 04:20:03.609621'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-03-28 04:20:04.143862'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-03-28 04:20:04.465077'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-03-28 04:20:04.783895'),
(9, 'auth', '0004_alter_user_username_opts', '2019-03-28 04:20:04.949677'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-03-28 04:20:05.236899'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-03-28 04:20:05.290568'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-03-28 04:20:05.358891'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-03-28 04:20:05.811210'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-03-28 04:20:06.126899'),
(15, 'authenticate', '0001_initial', '2019-03-28 04:20:08.544780'),
(16, 'chat', '0001_initial', '2019-03-28 04:20:10.491801'),
(17, 'programs', '0001_initial', '2019-03-28 04:20:10.607050'),
(18, 'sessions', '0001_initial', '2019-03-28 04:20:11.126706'),
(19, 'todo_list', '0001_initial', '2019-03-28 04:20:11.685626'),
(20, 'programs', '0002_programs_project_members', '2019-04-02 23:25:49.125244');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0hndbwxsu68z5ismujtupw9qf60yljp7', 'YWJmOTY0MDU2MzllY2E5MWM1ODMzYjVmOWE2ZjA1NjRhZTVlZjBiNzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzYTkzZWZjNGZiZWY1YThiOWFmMGVlZjlhNWZjMDNmNjc1ZmVjYWNjIn0=', '2019-04-11 15:34:13.037048'),
('3gs6l45dflluqvyl582ndml2f5zedo61', 'YWJmOTY0MDU2MzllY2E5MWM1ODMzYjVmOWE2ZjA1NjRhZTVlZjBiNzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzYTkzZWZjNGZiZWY1YThiOWFmMGVlZjlhNWZjMDNmNjc1ZmVjYWNjIn0=', '2019-04-11 14:29:08.230901'),
('8vfjw07l5sgd8dvdpv849ahgunv8z0ue', 'ZmFlZDlhYzBjMmY0YzY3YTFmMDliYWY3NDhjNTY3ZTQwNDU0M2Q3Yjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2MmJiN2JiYWJlZDIwYzI0ZjllY2UyZjIxNmMwNGM2OTRmNjRkYzY3In0=', '2019-04-17 04:16:44.771601'),
('8xafk65arj0e1qbt14awvk8p19cp170z', 'NWUxNTdlYTZiMDdkMzQyMDFhZDU0NTAzNDQ0MDA4MTNmMTBjNzA4ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNWNlNzcwMWEwZTIwOGRiOTAwNTJjMTQ1ZGUyMWU4MTY5OGYzODkyIn0=', '2019-04-17 04:16:57.410007'),
('qznsr0n3y6o5nvctnuejcc2f7sexfsql', 'ZmFlZDlhYzBjMmY0YzY3YTFmMDliYWY3NDhjNTY3ZTQwNDU0M2Q3Yjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2MmJiN2JiYWJlZDIwYzI0ZjllY2UyZjIxNmMwNGM2OTRmNjRkYzY3In0=', '2019-04-11 15:32:33.195826');

-- --------------------------------------------------------

--
-- Table structure for table `programs_programs`
--

CREATE TABLE `programs_programs` (
  `id` int(11) NOT NULL,
  `project_name` varchar(20) NOT NULL,
  `start_date` datetime(6) NOT NULL,
  `project_description` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `programs_programs`
--

INSERT INTO `programs_programs` (`id`, `project_name`, `start_date`, `project_description`) VALUES
(1, 'CS673_WebApplication', '2019-04-02 23:13:50.000000', 'Web application'),
(2, 'CS579', '2019-04-02 23:14:17.000000', 'DB_management'),
(3, 'CS100', '2019-04-02 23:16:12.000000', 'CS100_001');

-- --------------------------------------------------------

--
-- Table structure for table `programs_programs_project_members`
--

CREATE TABLE `programs_programs_project_members` (
  `id` int(11) NOT NULL,
  `programs_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `programs_programs_project_members`
--

INSERT INTO `programs_programs_project_members` (`id`, `programs_id`, `user_id`) VALUES
(2, 3, 3);

-- --------------------------------------------------------

--
-- Table structure for table `todo_list_list`
--

CREATE TABLE `todo_list_list` (
  `id` int(11) NOT NULL,
  `item` varchar(35) NOT NULL,
  `completed` tinyint(1) NOT NULL,
  `belongs_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `todo_list_list`
--

INSERT INTO `todo_list_list` (`id`, `item`, `completed`, `belongs_id`) VALUES
(1, 'CHAT ROOM', 0, 1),
(2, 'abcdefg', 0, 2),
(3, 'nothing', 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authenticate_friend`
--
ALTER TABLE `authenticate_friend`
  ADD PRIMARY KEY (`id`),
  ADD KEY `authenticate_friend_current_user_id_21671bdf_fk_auth_user_id` (`current_user_id`);

--
-- Indexes for table `authenticate_friend_users`
--
ALTER TABLE `authenticate_friend_users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `authenticate_friend_users_friend_id_user_id_8c1086b2_uniq` (`friend_id`,`user_id`),
  ADD KEY `authenticate_friend_users_user_id_80a24570_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `chat_chatmessage`
--
ALTER TABLE `chat_chatmessage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `chat_chatmessage_thread_id_0986d8f2_fk_chat_thread_id` (`thread_id`),
  ADD KEY `chat_chatmessage_user_id_fa615e65_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `chat_thread`
--
ALTER TABLE `chat_thread`
  ADD PRIMARY KEY (`id`),
  ADD KEY `chat_thread_first_id_f059d541_fk_auth_user_id` (`first_id`),
  ADD KEY `chat_thread_second_id_fb0dac48_fk_auth_user_id` (`second_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `programs_programs`
--
ALTER TABLE `programs_programs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `programs_programs_project_members`
--
ALTER TABLE `programs_programs_project_members`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `programs_programs_projec_programs_id_user_id_26fb05c1_uniq` (`programs_id`,`user_id`),
  ADD KEY `programs_programs_pr_user_id_5037b60a_fk_auth_user` (`user_id`);

--
-- Indexes for table `todo_list_list`
--
ALTER TABLE `todo_list_list`
  ADD PRIMARY KEY (`id`),
  ADD KEY `todo_list_list_belongs_id_67b634ce_fk_programs_programs_id` (`belongs_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `authenticate_friend`
--
ALTER TABLE `authenticate_friend`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `authenticate_friend_users`
--
ALTER TABLE `authenticate_friend_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `chat_chatmessage`
--
ALTER TABLE `chat_chatmessage`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT for table `chat_thread`
--
ALTER TABLE `chat_thread`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `programs_programs`
--
ALTER TABLE `programs_programs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `programs_programs_project_members`
--
ALTER TABLE `programs_programs_project_members`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `todo_list_list`
--
ALTER TABLE `todo_list_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `authenticate_friend`
--
ALTER TABLE `authenticate_friend`
  ADD CONSTRAINT `authenticate_friend_current_user_id_21671bdf_fk_auth_user_id` FOREIGN KEY (`current_user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `authenticate_friend_users`
--
ALTER TABLE `authenticate_friend_users`
  ADD CONSTRAINT `authenticate_friend__friend_id_722bda9b_fk_authentic` FOREIGN KEY (`friend_id`) REFERENCES `authenticate_friend` (`id`),
  ADD CONSTRAINT `authenticate_friend_users_user_id_80a24570_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `chat_chatmessage`
--
ALTER TABLE `chat_chatmessage`
  ADD CONSTRAINT `chat_chatmessage_thread_id_0986d8f2_fk_chat_thread_id` FOREIGN KEY (`thread_id`) REFERENCES `chat_thread` (`id`),
  ADD CONSTRAINT `chat_chatmessage_user_id_fa615e65_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `chat_thread`
--
ALTER TABLE `chat_thread`
  ADD CONSTRAINT `chat_thread_first_id_f059d541_fk_auth_user_id` FOREIGN KEY (`first_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `chat_thread_second_id_fb0dac48_fk_auth_user_id` FOREIGN KEY (`second_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `programs_programs_project_members`
--
ALTER TABLE `programs_programs_project_members`
  ADD CONSTRAINT `programs_programs_pr_programs_id_bc550ae2_fk_programs_` FOREIGN KEY (`programs_id`) REFERENCES `programs_programs` (`id`),
  ADD CONSTRAINT `programs_programs_pr_user_id_5037b60a_fk_auth_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `todo_list_list`
--
ALTER TABLE `todo_list_list`
  ADD CONSTRAINT `todo_list_list_belongs_id_67b634ce_fk_programs_programs_id` FOREIGN KEY (`belongs_id`) REFERENCES `programs_programs` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
